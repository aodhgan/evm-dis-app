import React from 'react';
import Link from 'next/link'

const FooterBanner = () => {
    return (
        <div className="footer-banner">
            {/* <a href="/faq" className="footer-link">FAQ</a>
             */}
            <Link href="/faq" className="footer-link">FAQ</Link>
            <span className="footer-text">Made with ❤️ by <a href="https://www.mantle.xyz/">Mantle Research Team</a></span>
        </div>
    );
};

export default FooterBanner;

