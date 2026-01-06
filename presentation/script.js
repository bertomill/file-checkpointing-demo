/* =============================================
   FILE CHECKPOINTING PRESENTATION
   Shared JavaScript
   ============================================= */

// Keyboard navigation
document.addEventListener('keydown', (e) => {
  const currentPage = window.location.pathname;

  if (e.key === 'ArrowRight' || e.key === ' ') {
    e.preventDefault();
    const nextBtn = document.querySelector('.next-btn');
    if (nextBtn) {
      nextBtn.click();
    }
  }

  if (e.key === 'ArrowLeft') {
    e.preventDefault();
    const backBtn = document.querySelector('.back-btn');
    if (backBtn) {
      backBtn.click();
    }
  }
});

// Add entrance animations
document.addEventListener('DOMContentLoaded', () => {
  // Fade in elements with stagger
  const content = document.querySelector('.content');
  if (content) {
    content.style.opacity = '0';
    content.style.transform = 'translateY(20px)';

    setTimeout(() => {
      content.style.transition = 'all 0.6s ease-out';
      content.style.opacity = '1';
      content.style.transform = 'translateY(0)';
    }, 100);
  }

  // Stagger animate features/items
  const staggerItems = document.querySelectorAll('.feature, .flow-step, .why-list li');
  staggerItems.forEach((item, index) => {
    item.style.opacity = '0';
    item.style.transform = 'translateY(20px)';

    setTimeout(() => {
      item.style.transition = 'all 0.4s ease-out';
      item.style.opacity = '1';
      item.style.transform = 'translateY(0)';
    }, 200 + (index * 100));
  });
});

// Smooth page transitions
document.querySelectorAll('a').forEach(link => {
  link.addEventListener('click', function(e) {
    if (this.hostname === window.location.hostname) {
      e.preventDefault();
      const href = this.href;

      document.body.style.opacity = '0';
      document.body.style.transition = 'opacity 0.2s ease-out';

      setTimeout(() => {
        window.location.href = href;
      }, 200);
    }
  });
});

// Restore opacity on page load
window.addEventListener('pageshow', () => {
  document.body.style.opacity = '1';
});
