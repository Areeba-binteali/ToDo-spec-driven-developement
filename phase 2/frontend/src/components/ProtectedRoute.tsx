import React, { useEffect, useState } from 'react';
import { useRouter } from 'next/router';
import { isAuthenticated } from '../services/authService';

interface ProtectedRouteProps {
  children: React.ReactNode;
}

const ProtectedRoute: React.FC<ProtectedRouteProps> = ({ children }) => {
  const router = useRouter();
  const [checkedAuth, setCheckedAuth] = useState(false);

  // Check if user is authenticated
  useEffect(() => {
    // Wait for the component to mount on the client before checking auth
    if (!isAuthenticated()) {
      // Redirect to login page if not authenticated
      router.push('/login');
    } else {
      setCheckedAuth(true);
    }
  }, [router]);

  // During SSR or before auth check, don't render anything
  if (typeof window === 'undefined' || !checkedAuth) {
    return (
      <div className="flex justify-center items-center h-screen">
        <p>Loading...</p>
      </div>
    );
  }

  // If authenticated, render the protected content
  return <>{children}</>;
};

export default ProtectedRoute;