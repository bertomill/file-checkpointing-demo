"""
Mountain Gear Co — Black Friday Sale Pricing Update
====================================================
This demo shows file checkpointing in action.

Run with:
  export CLAUDE_CODE_ENABLE_SDK_FILE_CHECKPOINTING=1
  python update_pricing.py
"""

import asyncio
import json
import os
from claude_agent_sdk import ClaudeSDKClient, ClaudeAgentOptions, UserMessage, ResultMessage


def show_pricing_summary(filepath: str):
    """Display current pricing from the config file."""
    with open(filepath, 'r') as f:
        config = json.load(f)

    print("\n" + "=" * 50)
    print(f"  {config['store_name']} — Current Pricing")
    print("=" * 50)

    # Show products with any applicable discounts
    discount_map = {}
    for rule in config['discount_rules']:
        if rule['type'] == 'category_discount' and rule['active']:
            discount_map[rule['target']] = rule['discount_percent']

    print("\n  Products:")
    print("  " + "-" * 46)

    for product in config['products']:
        discount = discount_map.get(product['category'], 0)
        base = product['base_price']

        if discount > 0:
            sale_price = base * (1 - discount / 100)
            print(f"  {product['name']:<25} ${base:>7.2f} → ${sale_price:.2f} ({discount}% off)")
        else:
            print(f"  {product['name']:<25} ${base:>7.2f}")

    # Show active rules
    print("\n  Active Rules:")
    print("  " + "-" * 46)

    for rule in config['discount_rules']:
        if rule['active']:
            if rule['type'] == 'category_discount':
                print(f"  • {rule['target'].title()}: {rule['discount_percent']}% off")
            elif rule['type'] == 'minimum_purchase':
                print(f"  • Orders ${rule['threshold_usd']}+: {rule['discount_percent']}% off")

    # Show shipping
    shipping = config.get('shipping', {})
    if shipping.get('free_shipping_threshold'):
        print(f"  • Free shipping on orders ${shipping['free_shipping_threshold']}+")
    else:
        print(f"  • Standard shipping: ${shipping.get('standard_rate', 'N/A')}")

    print()


async def main():
    config_file = "pricing_config.json"

    # Check if config file exists
    if not os.path.exists(config_file):
        print(f"Error: {config_file} not found. Please create it first.")
        return

    print("\n🏔️  Mountain Gear Co — Black Friday Sale Setup")
    print("=" * 50)

    # Show current state
    print("\n📋 BEFORE — Current pricing configuration:")
    show_pricing_summary(config_file)

    input("Press Enter to apply Black Friday sale pricing...")

    # Configure SDK with checkpointing
    options = ClaudeAgentOptions(
        enable_file_checkpointing=True,
        permission_mode="acceptEdits",
        extra_args={"replay-user-messages": None},
        env={**os.environ, "CLAUDE_CODE_ENABLE_SDK_FILE_CHECKPOINTING": "1"}
    )

    checkpoint_id = None
    session_id = None

    print("\n🤖 Running Claude to update pricing...")
    print("-" * 50)

    async with ClaudeSDKClient(options) as client:
        await client.query(f"""
            Update {config_file} for our Black Friday sale:

            1. Set camping category discount to 25%
            2. Set footwear category discount to 15%
            3. Add free shipping for orders over $150 (update free_shipping_threshold to 150)
            4. Update last_updated to today's date

            Keep all existing products and structure intact.
            Only modify the discount_percent values and shipping threshold.
        """)

        async for message in client.receive_response():
            # Capture the first user message UUID as our checkpoint
            if isinstance(message, UserMessage) and message.uuid and not checkpoint_id:
                checkpoint_id = message.uuid
                print(f"✓ Checkpoint captured: {checkpoint_id[:8]}...")

            # Capture session ID for potential rollback
            if isinstance(message, ResultMessage):
                session_id = message.session_id

    print("-" * 50)
    print("✅ Sale pricing applied!\n")

    # Show updated state
    print("📋 AFTER — Updated pricing configuration:")
    show_pricing_summary(config_file)

    # Decision point
    print("=" * 50)
    print("  DECISION POINT")
    print("=" * 50)
    print("\n  Options:")
    print("    [y] Keep these changes (go live with sale)")
    print("    [n] Rollback to original pricing")

    response = input("\n  Keep changes? (y/n): ").strip().lower()

    if response == "n" and checkpoint_id and session_id:
        print("\n↩️  Rolling back to original pricing...")

        async with ClaudeSDKClient(ClaudeAgentOptions(
            enable_file_checkpointing=True,
            resume=session_id
        )) as client:
            await client.query("")
            async for message in client.receive_response():
                await client.rewind_files(checkpoint_id)
                break

        print("✓ Rollback complete!\n")
        print("📋 RESTORED — Original pricing:")
        show_pricing_summary(config_file)

    elif response == "y":
        print("\n🚀 Changes approved! Black Friday sale is now live.")
        print("   Customers will see the new pricing immediately.\n")
    else:
        print("\n⚠️  Invalid input. Changes kept by default.\n")


if __name__ == "__main__":
    asyncio.run(main())
