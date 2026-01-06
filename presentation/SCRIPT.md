# File Checkpointing Presentation Script

**Total Runtime:** ~4-5 minutes
**Tone:** Friendly, educational, enthusiastic but not over-the-top

---

## PAGE 1: Introduction
**[SCREEN: Title slide with "File Checkpointing" and animated file icon]**

### Opening Hook (10 seconds)
> "What if I told you there's a way to let AI edit your files... and undo everything with a single line of code?"

### Introduction (30 seconds)
> "Hey everyone! Today we're diving into one of my favorite features in the Claude Agent SDK — File Checkpointing.
>
> If you're building applications where Claude edits files — whether that's config files, code, documents, whatever — this feature is a game-changer.
>
> Here's what it lets you do:"

**[SCREEN: Features appear one by one]**

> "First — **Rewind Changes**. Restore any file to exactly how it was before Claude touched it.
>
> Second — **Experiment Freely**. Try out ideas without worrying about breaking things.
>
> And third — **Recover from Errors**. If Claude makes a mistake, one command brings everything back."

### The Flow (20 seconds)
**[SCREEN: Show the 1-2-3 concept flow]**

> "The concept is simple:
>
> Step one — Claude edits your files using the Write, Edit, or NotebookEdit tools.
>
> Step two — The SDK automatically saves checkpoints as it goes.
>
> Step three — Anytime you want, you call rewind, and boom — files restored.
>
> Let's see this in action, but first..."

---

## PAGE 2: Like & Subscribe
**[SCREEN: Subscribe page with mission statement]**

### The Ask (25 seconds)
> "Before we jump into the demo, I want to take a quick second.
>
> If you're watching this, you're probably someone who's passionate about building things with AI. That's exactly who we make these videos for.
>
> Our mission is to help passionate people — whether you're a solo developer, running a small business, or part of an enterprise team — actually build real things with these tools.
>
> So if that sounds like you..."

**[SCREEN: Highlight the buttons]**

> "Hit that like button, subscribe if you haven't already, and turn on notifications so you don't miss the next one.
>
> We've got weekly tutorials, real-world examples, and we're always covering the latest SDK features.
>
> Alright, let's get to the good stuff."

---

## PAGE 3: Interactive Demo
**[SCREEN: Demo page with Mountain Gear Co pricing config]**

### Setting the Scene (20 seconds)
> "Okay, here's a real-world scenario.
>
> Let's say you run an e-commerce store — Mountain Gear Co — and Black Friday is coming up.
>
> You want Claude to update your pricing config: 25% off camping gear, 15% off footwear, and add free shipping for orders over 150 bucks.
>
> But here's the thing — what if Claude makes a mistake? What if the discounts are wrong? What if something breaks?"

### The Demo (60 seconds)
**[SCREEN: Click "Apply Black Friday Sale" button]**

> "Watch this. I'm going to click 'Apply Black Friday Sale.'
>
> First thing that happens — a checkpoint is saved. See that? The SDK captured the original state of our file before any changes.
>
> Now Claude is working... updating the camping discount... footwear discount... adding the free shipping rule..."

**[SCREEN: Show the updated pricing with discounts]**

> "And there it is! Look at that — our 2-Person Tent went from $199 to $149. Hiking boots from $149 to $127. The free shipping rule is now active.
>
> All the changes are applied. But here's where the magic happens..."

**[SCREEN: Click "Rewind to Checkpoint" button]**

> "Let's say I don't like these changes. Maybe I want to try different discount percentages. I click 'Rewind to Checkpoint' and..."

**[SCREEN: Show the restored original pricing]**

> "Boom. Everything is back to exactly how it was. Original prices, no discounts, no free shipping rule. One click. That's it."

### The Code (20 seconds)
**[SCREEN: Highlight the code snippet]**

> "And in your code, it's literally this simple:
>
> `await client.rewind_files(checkpoint_id)`
>
> That's one line. You pass in the checkpoint ID you saved earlier, and the SDK handles everything — deleting files that were created, restoring files that were modified, all of it."

### Q&A - Addressing Common Questions (45 seconds)
**[SCREEN: Q&A section - First question]**

> "Now let's tackle some questions you might have.
>
> First one: Do I need to manually create a checkpoint after every step?
>
> **No.** The SDK handles it automatically. When you enable `enable_file_checkpointing=True`, the SDK creates backups before any file modification. Each user message in the response stream comes with a UUID — that's your checkpoint.
>
> Think of it like auto-save in a video game. The system is constantly saving. You just decide when to load a previous save."

**[SCREEN: Q&A section - Second question]**

> "Second question: What if I don't use checkpointing at all?
>
> Well... you're on your own for recovery.
>
> Without checkpointing, if Claude makes unwanted changes, you'd have to manually undo in your editor — Cmd+Z a bunch of times — or use Git to restore files, or keep manual backups before every operation.
>
> Checkpointing gives you a one-line safety net. No Git gymnastics. No manual backups. No stress."

**[SCREEN: Q&A section - Third question]**

> "And I know what you're thinking — why can't I just hit Cmd+Z?
>
> Here's the thing: Cmd+Z doesn't scale.
>
> It only works in one file at a time. If Claude edited five files, you'd have to open each one and undo separately.
>
> Close the file? Undo history is gone. Claude created new files? Cmd+Z won't delete them.
>
> Checkpointing gives you one command that restores everything — all files, all changes, instantly. It's like Cmd+Z for your entire project."

### What It Looks Like in Code (35 seconds)
**[SCREEN: Code section with 3 steps]**

> "So let's look at the actual code. It's surprisingly simple.
>
> **Step one** — Enable checkpointing. You add `enable_file_checkpointing=True` to your options. That's it for config.

**[SCREEN: Highlight Step 1 code]**

> "**Step two** — Capture the checkpoint ID. As you loop through the response, you grab the UUID from the first user message. That's your restore point.

**[SCREEN: Highlight Step 2 code]**

> "**Step three** — Rewind when needed. One line: `await client.rewind_files(checkpoint_id)`. Done.

**[SCREEN: Highlight Step 3 code and summary]**

> "That's it. Three lines of config. One line to capture. One line to rewind. Your entire project can now time travel."

---

## PAGE 4: Takeaways & Next Steps
**[SCREEN: Takeaways page]**

### Key Takeaways (30 seconds)
> "Alright, let's recap what we learned today.
>
> **Number one** — Checkpointing is your safety net. Let Claude edit files with confidence because you can always roll back.
>
> **Number two** — Capture those UUIDs. Every user message in the response stream has a UUID. That's your restore point. Save it before risky operations.
>
> **Number three** — One line to rewind. That's all it takes. `rewind_files`, pass the checkpoint ID, done."

### Where to Apply (25 seconds)
**[SCREEN: Show the application cards]**

> "So where can you actually use this?
>
> **E-commerce** — Update pricing, inventory, product configs, knowing you can roll back instantly.
>
> **Document generation** — Generate contracts, invoices, reports. If the formatting breaks, rewind.
>
> **Infrastructure** — Modify your Terraform files, Docker configs, Kubernetes manifests. If something's wrong, restore.
>
> **Code refactoring** — Let AI refactor your entire codebase. If the tests fail, roll back everything."

### Next Steps (20 seconds)
**[SCREEN: Show next steps links]**

> "Here's what I want you to do next:
>
> First, check out the official docs. I'll link them below. Everything we covered today and more.
>
> Second, install the SDK if you haven't. Pip install or npm install, takes 30 seconds.
>
> And third — and this is the important one — **build something**. Start small. A config file updater. A document generator. Something simple. Then expand from there."

### Closing (15 seconds)
**[SCREEN: Share buttons and closing message]**

> "If this video helped you, share it with someone who's building with AI. We're all learning together.
>
> Thanks for watching, and I'll see you in the next one. Now go build something amazing."

**[END]**

---

## Production Notes

### B-Roll Suggestions
- Screen recordings of the actual demo
- Code editor showing the Python/TypeScript implementation
- Terminal showing the SDK installation
- Anthropic docs website

### Graphics Needed
- Animated checkpoint icon
- Before/after file comparison
- Flow diagram animation

### Music
- Upbeat but not distracting
- Lower during explanations
- Bump up during transitions

### Timestamps for Description
```
0:00 - Introduction
0:40 - How Checkpointing Works
1:20 - Quick Message
1:45 - Live Demo
3:00 - Key Takeaways
3:45 - Where to Apply This
4:15 - Your Next Steps
```

---

## Thumbnail Ideas

1. Split screen: "BEFORE" (broken code) / "AFTER" (clean code) with rewind arrow
2. Big text: "UNDO AI MISTAKES" with Claude logo
3. Your face + shocked expression + "One Line of Code"
