import React from 'react';
import Link from 'next/link';
import Layout from '../components/Layout';

const TermsPage: React.FC = () => {
  return (
    <Layout title="Terms and Conditions">
      <div className="min-h-screen bg-black">
        <div className="max-w-4xl mx-auto px-4 py-16">
          <div className="text-center mb-12">
            <h1 className="text-4xl font-bold text-white mb-4">
              <span className="text-[#00a5bb]">
                Terms and Conditions
              </span>
            </h1>
            <p className="text-white">Please read these terms carefully before using our service</p>
          </div>

          <div className="bg-black rounded-2xl shadow-xl p-8 border-2 border-[#00a5bb]">
            <div className="prose max-w-none">
              <h2 className="text-2xl font-bold text-white mb-6">1. Introduction</h2>
              <p className="text-white mb-6">
                Welcome to TodoApp. These terms and conditions outline the rules and regulations for the use of our application.
              </p>

              <h2 className="text-2xl font-bold text-white mb-6">2. Intellectual Property</h2>
              <p className="text-white mb-6">
                Unless otherwise stated, TodoApp and/or its licensors own the intellectual property rights for all material on TodoApp. All intellectual property rights are reserved.
              </p>

              <h2 className="text-2xl font-bold text-white mb-6">3. Restrictions</h2>
              <p className="text-white mb-4">
                You are specifically restricted from all of the following:
              </p>
              <ul className="list-disc pl-6 mb-6 text-white space-y-2">
                <li>Publishing any material on TodoApp in any way that is misleading or fraudulent</li>
                <li>Using this application in any way that impacts user access</li>
                <li>Engaging in any data mining or similar extraction activities</li>
                <li>Attempting to gain unauthorized access to other accounts</li>
              </ul>

              <h2 className="text-2xl font-bold text-white mb-6">4. Limitation of Liability</h2>
              <p className="text-white mb-6">
                TodoApp shall not be held liable for any consequential, incidental, indirect, or special damages arising out of your use of this application.
              </p>

              <h2 className="text-2xl font-bold text-white mb-6">5. Changes to Terms</h2>
              <p className="text-white mb-8">
                We reserve the right to modify these terms at any time. Continued use of the application after changes constitutes acceptance of the new terms.
              </p>
            </div>

            <div className="flex flex-col sm:flex-row gap-4 pt-6">
              <Link href="/" className="btn-primary text-center">
                Back to Home
              </Link>
              <Link href="/privacy" className="btn-outline text-center">
                Privacy Policy
              </Link>
            </div>
          </div>
        </div>
      </div>
    </Layout>
  );
};

export default TermsPage;