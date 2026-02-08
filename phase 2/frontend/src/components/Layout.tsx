import React from 'react';
import Head from 'next/head';
import Link from 'next/link';
import { useRouter } from 'next/router';
import { isAuthenticated, logout } from '../services/authService';

interface LayoutProps {
  children: React.ReactNode;
  title?: string;
}

const Layout: React.FC<LayoutProps> = ({ children, title = 'Todo App' }) => {
  const router = useRouter();
  const isLoggedIn = isAuthenticated();

  const handleLogout = () => {
    logout();
    router.push('/login');
  };

  return (
    <>
      <Head>
        <title>{title}</title>
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <meta name="description" content="Todo application for managing your tasks" />
      </Head>
      <div className="min-h-screen bg-black">
        {/* Header */}
        <header className="bg-black shadow-lg shadow-[#00a5bb] border-b-2 border-[#00a5bb]">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div className="flex justify-between h-16 items-center">
              <div className="flex items-center">
                <Link href="/">
                  <h1 className="text-2xl font-bold text-[#00a5bb] hover:text-white cursor-pointer">Todo<span className="text-white">App</span></h1>
                </Link>
              </div>
              <nav className="hidden md:block">
                <ul className="flex space-x-8">
                  <li>
                    <Link href="/">
                      <span className={`cursor-pointer transition-colors duration-200 ${router.pathname === '/' ? 'text-[#00a5bb] font-semibold' : 'text-white hover:text-[#00a5bb]'}`}>
                        Home
                      </span>
                    </Link>
                  </li>
                  {!isLoggedIn && (
                    <>
                      <li>
                        <Link href="/terms">
                          <span className={`cursor-pointer transition-colors duration-200 ${router.pathname === '/terms' ? 'text-[#00a5bb] font-semibold' : 'text-white hover:text-[#00a5bb]'}`}>
                          Terms
                        </span>
                      </Link>
                    </li>
                    <li>
                      <Link href="/privacy">
                        <span className={`cursor-pointer transition-colors duration-200 ${router.pathname === '/privacy' ? 'text-[#00a5bb] font-semibold' : 'text-white hover:text-[#00a5bb]'}`}>
                          Privacy
                        </span>
                      </Link>
                    </li>
                    </>
                  )}
                  {isLoggedIn && (
                    <>
                      <li>
                        <Link href="/dashboard">
                          <span className={`cursor-pointer transition-colors duration-200 ${router.pathname === '/dashboard' ? 'text-[#00a5bb] font-semibold' : 'text-white hover:text-[#00a5bb]'}`}>
                            Dashboard
                          </span>
                        </Link>
                      </li>
                      <li>
                        <Link href="/profile">
                          <span className={`cursor-pointer transition-colors duration-200 ${router.pathname === '/profile' ? 'text-[#00a5bb] font-semibold' : 'text-white hover:text-[#00a5bb]'}`}>
                            Profile
                          </span>
                        </Link>
                      </li>
                    </>
                  )}
                </ul>
              </nav>
              <div className="flex items-center space-x-4">
                {!isLoggedIn ? (
                  <>
                    <Link href="/login">
                      <span className="text-white hover:text-[#00a5bb] font-medium cursor-pointer transition-colors duration-200 no-underline">
                        Login
                      </span>
                    </Link>
                    <Link href="/register">
                      <span className="ml-4 btn-primary no-underline">
                        Register
                      </span>
                    </Link>
                  </>
                ) : (
                  <>
                    <Link href="/dashboard">
                      <span className="text-white hover:text-[#00a5bb] font-medium cursor-pointer transition-colors duration-200 no-underline">
                        Dashboard
                      </span>
                    </Link>
                    <Link href="/profile">
                      <span className="ml-4 text-white hover:text-[#00bcd4] font-medium cursor-pointer transition-colors duration-200 no-underline">
                        Profile
                      </span>
                    </Link>
                    <button
                      onClick={handleLogout}
                      className="ml-4 btn-secondary"
                    >
                      Logout
                    </button>
                  </>
                )}
              </div>
            </div>
          </div>
        </header>

        {/* Main content */}
        <main className="max-w-7xl mx-auto py-8 sm:px-6 lg:px-8">
          <div className="px-4 py-6 sm:px-0">
            {children}
          </div>
        </main>

        {/* Footer */}
        <footer className="bg-black mt-12 border-t border-[#00a5bb] shadow-inner">
          <div className="max-w-7xl mx-auto py-6 px-4 sm:px-6 lg:px-8">
            <div className="md:flex md:items-center md:justify-between">
              <div className="flex justify-center md:justify-start">
                <div className="flex items-center">
                  <span className="text-xl font-bold text-[#00a5bb]">Todo<span className="text-white">App</span></span>
                </div>
              </div>
              <div className="mt-4 md:mt-0">
                <p className="text-center text-sm text-white">
                  © {new Date().getFullYear()} TodoApp. All rights reserved.
                </p>
              </div>
            </div>
          </div>
        </footer>
      </div>
    </>
  );
};

export default Layout;