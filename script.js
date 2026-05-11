// 分頁功能
document.addEventListener('DOMContentLoaded', function() {
    // 導航連結點擊事件（包含 logo-link）
    const navLinks = document.querySelectorAll('.nav-link, .logo-link');
    
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            
            // 獲取目標區塊 ID
            const targetId = this.getAttribute('href').substring(1);
            const targetSection = document.getElementById(targetId);
            
            // 先移除所有 active 類別（但保留首頁）
            const allNavLinks = document.querySelectorAll('.nav-link, .logo-link');
            allNavLinks.forEach(l => l.classList.remove('active'));
            const homeSection = document.getElementById('home');
            document.querySelectorAll('.page-section').forEach(s => {
                if (s.id !== 'home') s.classList.remove('active');
            });
            
            // 添加 active 類別到點擊的連結
            this.classList.add('active');
            
            // 先顯示目標區塊，再滾動
            targetSection.classList.add('active');
            
            // 使用 setTimeout 確保 DOM 更新完成後再滾動
            setTimeout(() => {
                // 如果是回到首頁，需要滾動到首頁位置
                if (targetId === 'home') {
                    targetSection.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                    const otherSections = document.querySelectorAll('.page-section:not(#home)');
                    otherSections.forEach(s => s.classList.remove('active'));
                } else {
                    targetSection.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                    
                    // 滾動完成後再切換首頁顯示狀態
                    setTimeout(() => {
                        homeSection.classList.remove('active');
                    }, 3000);
                }
            }, 10);
        });
    });

    // 滾動時更新導航連結的 active 狀態
    window.addEventListener('scroll', function() {
        const sections = document.querySelectorAll('.page-section');
        const navLinks = document.querySelectorAll('.nav-link, .logo-link');
        
        let current = '';
        
        sections.forEach(section => {
            // 計算當前滾動位置，減去固定導航欄的高度，以獲得相對於內容區域的實際偏移量。
            const fixedHeaderHeight = document.querySelector('.navbar')?.offsetHeight || 0;
            const sectionTopOffset = section.offsetTop - fixedHeaderHeight;
            // 判斷當前滾動位置是否接近區塊頂部 (使用一個小的緩衝值，例如 100px)
            if (pageY >= (sectionTopOffset - 100)) {
                current = section.getAttribute('id');
            } else if (pageY < (sectionTopOffset + section.clientHeight / 2)) {
                // 如果滾動位置在區塊前半部分，但還沒達到觸發點，則不更新 current。
                // 這可以防止在頁面頂部時誤判為第一個區塊。
            }
        });
        
        navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href').includes(current)) {
                link.classList.add('active');
            }
        });
    });

    // 平滑滾動支援舊瀏覽器
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });

    // 圖片懶加載
    const images = document.querySelectorAll('img[loading="lazy"]');
    images.forEach(img => {
        img.src = img.dataset.src || img.src;
    });

    // 顯示聯絡資訊按鈕（只針對第一個教練專線按鈕）
    const contactBtn = document.querySelector('.cta-button:not(.line-button)');
    if (contactBtn) {
        contactBtn.addEventListener('click', function() {
            const contactSection = document.getElementById('contact');
            contactSection.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        });
    }

    // 圖片點擊放大
    const imageModal = document.getElementById('imageModal');
    const modalImage = imageModal?.querySelector('img');
    const modalClose = imageModal?.querySelector('.modal-close');
    document.querySelectorAll('.exam-thumb, .about-img, .safety-training-img').forEach(img => {
        img.addEventListener('click', function() {
            if (!imageModal || !modalImage) return;
            modalImage.src = this.src;
            modalImage.alt = this.alt;
            imageModal.classList.add('open');
            document.body.style.overflow = 'hidden';
        });
    });

    const closeModal = () => {
        if (!imageModal) return;
        imageModal.classList.remove('open');
        document.body.style.overflow = '';
    };

    if (imageModal) {
        imageModal.addEventListener('click', function(event) {
            if (event.target === imageModal || event.target === modalClose) {
                closeModal();
            }
        });
    }

    document.addEventListener('keydown', function(event) {
        if (event.key === 'Escape') {
            closeModal();
        }
    });
});

// 簡單的動畫效果
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

// 為所有卡片添加動畫
document.querySelectorAll('.feature-card, .course-card, .vehicle-card, .exam-card, .medical-card, .video-card, .contact-item').forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(20px)';
    el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
    observer.observe(el);
});

