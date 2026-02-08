import React from 'react';
import Link from 'next/link';
import Layout from '../components/Layout';

const PrivacyPage: React.FC = () => {
  return (
    <Layout title="Privacy Policy">
      <div className="min-h-screen bg-black">
        <div className="max-w-4xl mx-auto px-4 py-16">
          <div className="text-center mb-12">
            <h1 className="text-4xl font-bold text-white mb-4">
              <span className="text-[#00a5bb]">
                Privacy Policy
              </span>
            </h1>
            <p className="text-white">How we collect, use, and protect your information</p>
          </div>

          <div className="bg-black rounded-2xl shadow-xl p-8 border-2 border-[#00a5bb]">
            <div className="prose max-w-none">
              <h2 className="text-2xl font-bold text-white mb-6">1. Information We Collect</h2>
              <p className="text-white mb-6">
                We collect information you provide directly to us, such as when you create an account, use our services, or contact us for support. This may include your name, email address, and other information you choose to provide.
              </p>

              <h2 className="text-2xl font-bold text-white mb-6">2. How We Use Your Information</h2>
              <p className="text-white mb-4">
                We use the information we collect to:
              </p>
              <ul className="list-disc pl-6 mb-6 text-white space-y-2">
                <li>Provide, maintain, and improve our services</li>
                <li>Communicate with you about your account</li>
                <li>Send you technical notices and support messages</li>
                <li>Protect against fraud and abuse</li>
              </ul>

              <h2 className="text-2xl font-bold text-white mb-6">3. Data Security</h2>
              <p className="text-white mb-6">
                We implement appropriate security measures to protect against unauthorized access, alteration, disclosure, or destruction of your personal information.
              </p>

              <h2 className="text-2xl font-bold text-white mb-6">4. Data Retention</h2>
              <p className="text-white mb-6">
                We retain your personal information for as long as necessary to provide our services and comply with legal obligations. When no longer needed, we securely delete your information.
              </p>

              <h2 className="text-2xl font-bold text-white mb-6">5. Your Rights</h2>
              <p className="text-white mb-4">
                Depending on your location, you may have the right to:
              </p>
              <ul className="list-disc pl-6 mb-6 text-white space-y-2">
                <li>Access your personal information</li>
                <li>Correct inaccurate data</li>
                <li>Request deletion of your data</li>
                <li>Object to processing of your data</li>
              </ul>

              <h2 className="text-2xl font-bold text-white mb-6">6. Contact Us</h2>
              <p className="text-gray-700 mb-8">
                If you have questions about this privacy policy, please contact us at privacy@todoapp.com.
              </p>
            </div>

            <div className="flex flex-col sm:flex-row gap-4 pt-6">
              <Link href="/" className="btn-primary text-center">
                Back to Home
              </Link>
              <Link href="/terms" className="btn-outline text-center">
                Terms & Conditions
              </Link>
            </div>
          </div>
        </div>
      </div>
    </Layout>
  );
};

export default PrivacyPage;