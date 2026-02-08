import React, { useState, useEffect } from 'react';
import { useRouter } from 'next/router';
import Link from 'next/link';
import { isAuthenticated } from '../services/authService';
import Layout from '../components/Layout';

const HomePage: React.FC = () => {
  const router = useRouter();

  const [loadingAuth, setLoadingAuth] = useState(true);

  useEffect(() => {
    // Delay the authentication check until after component mounts
    const checkAuth = async () => {
      await new Promise(resolve => setTimeout(resolve, 0)); // Ensures client-side execution

      if (isAuthenticated()) {
        router.push('/dashboard');
      } else {
        setLoadingAuth(false);
      }
    };

    checkAuth();
  }, []);

  // Show loading state while checking authentication
  if (loadingAuth) {
    return (
      <div className="flex justify-center items-center h-screen">
        <p>Loading...</p>
      </div>
    );
  }

  return (
    <Layout>
      <div className="min-h-screen bg-black">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
          <div className="text-center">
            <h1 className="text-4xl md:text-6xl font-extrabold text-white mb-6">
              <span className="text-[#00a5bb]">
                Organize Your Life
              </span>
            </h1>
            <p className="text-xl text-white max-w-3xl mx-auto mb-10">
              The ultimate todo app designed for productivity and simplicity.
              Get things done faster and smarter with our intuitive platform.
            </p>

            <div className="mb-16">
              <div className="inline-block bg-black rounded-2xl shadow-xl p-1 border border-[#00a5bb]">
                <div className="flex space-x-2">
                  <div className="w-3 h-3 rounded-full bg-[#00a5bb]"></div>
                  <div className="w-3 h-3 rounded-full bg-[#00a5bb]"></div>
                  <div className="w-3 h-3 rounded-full bg-[#00a5bb]"></div>
                </div>
                <div className="p-6">
                  <div className="bg-black border-2 border-dashed border-[#00a5bb] rounded-xl w-full h-64 flex items-center justify-center text-[#00a5bb]">
                    Todo Preview
                  </div>
                </div>
              </div>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-3 gap-8 mb-16">
              <div className="bg-black p-6 rounded-xl shadow-lg border border-[#00a5bb] transform hover:-translate-y-1 transition duration-300">
                <div className="text-[#00a5bb] mb-4">
                  <svg xmlns="http://www.w3.org/2000/svg" className="h-12 w-12 mx-auto" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
                  </svg>
                </div>
                <h3 className="text-xl font-bold text-white mb-2">Task Management</h3>
                <p className="text-[#00a5bb]">Easily create, organize, and track your tasks with our intuitive interface.</p>
              </div>

              <div className="bg-black p-6 rounded-xl shadow-lg border border-[#00a5bb] transform hover:-translate-y-1 transition duration-300">
                <div className="text-[#00a5bb] mb-4">
                  <svg xmlns="http://www.w3.org/2000/svg" className="h-12 w-12 mx-auto" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
                  </svg>
                </div>
                <h3 className="text-xl font-bold text-white mb-2">Time Tracking</h3>
                <p className="text-[#00a5bb]">Keep track of time spent on tasks to boost your productivity.</p>
              </div>

              <div className="bg-black p-6 rounded-xl shadow-lg border border-[#00a5bb] transform hover:-translate-y-1 transition duration-300">
                <div className="text-[#00a5bb] mb-4">
                  <svg xmlns="http://www.w3.org/2000/svg" className="h-12 w-12 mx-auto" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
                  </svg>
                </div>
                <h3 className="text-xl font-bold text-white mb-2">Secure & Private</h3>
                <p className="text-[#00a5bb]">Your data is encrypted and secure with our advanced security measures.</p>
              </div>
            </div>

            <div className="flex flex-col sm:flex-row justify-center gap-4">
              <Link href="/register" className="px-8 py-4 bg-[#00a5bb] text-white font-bold rounded-xl shadow-lg hover:shadow-xl transform hover:scale-105 transition duration-300 text-center no-underline border-2 border-[#000]">
                Get Started
              </Link>
              <Link href="/login" className="px-8 py-4 bg-[#000] text-white font-bold rounded-xl shadow-lg hover:shadow-xl border-2 border-[#00a5bb] transform hover:scale-105 transition duration-300 text-center no-underline">
                Sign In
              </Link>
            </div>
          </div>
        </div>

        <div className="bg-black py-12 border-t border-[#00a5bb]">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div className="text-center">
              <h2 className="text-3xl font-extrabold text-white mb-4">Trusted by thousands of users</h2>
              <p className="text-[#00a5bb] max-w-2xl mx-auto">Join our community of productive individuals who manage their tasks efficiently.</p>
            </div>
          </div>
        </div>
      </div>
    </Layout>
  );
};

export default HomePage;