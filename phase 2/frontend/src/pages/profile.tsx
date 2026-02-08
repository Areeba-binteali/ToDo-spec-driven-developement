import React, { useState, useEffect } from 'react';
import { useRouter } from 'next/router';
import { isAuthenticated, getToken, getUserInfo, logout } from '../services/authService';
import Layout from '../components/Layout';
// Removed ProtectedRoute import since we're handling auth ourselves

const ProfilePage: React.FC = () => {
  const router = useRouter();
  const [userInfo, setUserInfo] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [loadingAuth, setLoadingAuth] = useState(true);

  const handleLogout = () => {
    logout();
    router.push('/login');
  };

  useEffect(() => {
    // Delay the authentication check until after component mounts
    const checkAuth = async () => {
      await new Promise(resolve => setTimeout(resolve, 0)); // Ensures client-side execution

      if (!isAuthenticated()) {
        router.push('/login');
      } else {
        setLoadingAuth(false);
      }
    };

    checkAuth();
  }, []);

  useEffect(() => {
    if (!loadingAuth) { // Only run if authentication check is complete and user is logged in
      const user = getUserInfo();
      if (user) {
        setUserInfo(user);
      }
      setLoading(false);
    }
  }, [loadingAuth]); // Rerun when loadingAuth changes

  return (
    <Layout title="Profile">
      <div className="min-h-screen bg-black">
        {(loadingAuth || loading) ? (
          <div className="flex justify-center items-center h-screen">
            <div className="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-[#00a5bb]"></div>
          </div>
        ) : (
          <div className="max-w-4xl mx-auto px-4 py-8">
            <div className="text-center mb-10">
              <h1 className="text-4xl font-bold text-white mb-2">
                Your Profile
              </h1>
              <p className="text-white">Manage your account settings and preferences</p>
            </div>

            <div className="bg-black rounded-2xl shadow-xl p-8 border-2 border-[#00a5bb] max-w-2xl mx-auto">
              <div className="flex flex-col items-center mb-8">
                <div className="w-24 h-24 bg-[#00a5bb] rounded-full flex items-center justify-center mb-4">
                  <span className="text-3xl font-bold text-[#000]">
                    {userInfo?.email ? userInfo.email.charAt(0).toUpperCase() : '?'}
                  </span>
                </div>
                <h2 className="text-2xl font-bold text-white">
                  {userInfo?.email || 'User Profile'}
                </h2>
                <p className="text-white">Member since {userInfo?.iat ? new Date(userInfo.iat * 1000).toLocaleDateString() : 'Unknown'}</p>
              </div>

              <div className="space-y-6">
                <div className="bg-black p-6 rounded-xl border border-[#00a5bb]">
                  <h3 className="text-lg font-semibold text-white mb-4">Account Information</h3>
                  <div className="space-y-3">
                    <div className="flex justify-between">
                      <span className="text-white">Email</span>
                      <span className="font-medium text-white">{userInfo?.email || 'N/A'}</span>
                    </div>
                    <div className="flex justify-between">
                      <span className="text-white">Account Type</span>
                      <span className="font-medium text-white">Free</span>
                    </div>
                    <div className="flex justify-between">
                      <span className="text-white">Member Since</span>
                      <span className="font-medium text-white">
                        {userInfo?.iat ? new Date(userInfo.iat * 1000).toLocaleDateString() : 'N/A'}
                      </span>
                    </div>
                  </div>
                </div>

                <div className="bg-black p-6 rounded-xl border border-[#00a5bb]">
                  <h3 className="text-lg font-semibold text-white mb-4">Security</h3>
                  <div className="space-y-3">
                    <button className="w-full text-left py-2 text-[#00a5bb] hover:text-white transition-colors duration-200">
                      Change Password
                    </button>
                    <button className="w-full text-left py-2 text-[#00a5bb] hover:text-white transition-colors duration-200">
                      Two-Factor Authentication
                    </button>
                    <button className="w-full text-left py-2 text-[#00a5bb] hover:text-white transition-colors duration-200">
                      Active Sessions
                    </button>
                  </div>
                </div>

                <div className="pt-4">
                  <button
                    onClick={handleLogout}
                    className="btn-secondary w-full"
                  >
                    Log Out
                  </button>
                </div>
              </div>
            </div>
          </div>
        )}
      </div>
    </Layout>
  );
};

export default ProfilePage;
