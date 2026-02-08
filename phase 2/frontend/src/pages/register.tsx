import React, { useState, useEffect } from 'react';
import { useRouter } from 'next/router';
import UserRegistrationForm from '../components/UserRegistrationForm';
import Layout from '../components/Layout';
import { isAuthenticated } from '../services/authService';

const RegisterPage: React.FC = () => {
  const router = useRouter();
  const [loadingAuth, setLoadingAuth] = useState(true);
  const [isAlreadyLoggedIn, setIsAlreadyLoggedIn] = useState(false);

  useEffect(() => {
    // Delay the authentication check until after component mounts
    const checkAuth = async () => {
      await new Promise(resolve => setTimeout(resolve, 0)); // Ensures client-side execution

      if (isAuthenticated()) {
        // Redirect to dashboard if already logged in
        router.push('/dashboard');
        setIsAlreadyLoggedIn(true);
      } else {
        setLoadingAuth(false);
      }
    };

    checkAuth();
  }, [router]);

  const handleRegisterSuccess = () => {
    // Redirect to login after successful registration
    router.push('/login');
  };

  // Show loading state while checking authentication
  if (loadingAuth || isAlreadyLoggedIn) {
    return (
      <div className="flex justify-center items-center h-screen">
        <p>Loading...</p>
      </div>
    );
  }

  return (
    <Layout title="Register">
      <div className="form-wrapper">
        <div className="form-card bg-black border-2 border-[#00a5bb]">
          <div>
            <h2 className="mt-6 text-center text-3xl font-extrabold text-white">
              Create a new account
            </h2>
            <p className="mt-2 text-center text-sm text-white">
              Or{' '}
              <a href="/login" className="font-medium text-[#00a5bb] hover:text-white no-underline">
                sign in to your existing account
              </a>
            </p>
          </div>
          <UserRegistrationForm onRegisterSuccess={handleRegisterSuccess} />
          <div className="text-center">
            <p className="text-sm text-gray-600">
              Already have an account?{' '}
              <a href="/login" className="font-medium text-[#00a5bb] hover:text-white no-underline">
                Login here
              </a>
            </p>
          </div>
        </div>
      </div>
    </Layout>
  );
};

export default RegisterPage;