// Authentication service for managing user authentication state

// Check if user is authenticated
export const isAuthenticated = (): boolean => {
  if (typeof window === 'undefined') {
    // Server-side, return false
    return false;
  }
  const token = localStorage.getItem('access_token');
  return !!token;
};

// Get the current user token
export const getToken = (): string | null => {
  if (typeof window === 'undefined') {
    // Server-side, return null
    return null;
  }
  return localStorage.getItem('access_token');
};

// Save the user token
export const saveToken = (token: string): void => {
  if (typeof window !== 'undefined') {
    localStorage.setItem('access_token', token);
  }
};

// Remove the user token (logout)
export const removeToken = (): void => {
  if (typeof window !== 'undefined') {
    localStorage.removeItem('access_token');
  }
};

// Get user info from token (decode JWT)
export const getUserInfo = (): any => {
  if (typeof window === 'undefined') {
    // Server-side, return null
    return null;
  }
  const token = getToken();
  if (!token) {
    return null;
  }

  try {
    // Decode the JWT token to get user info
    const base64Url = token.split('.')[1];
    const base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
    const jsonPayload = decodeURIComponent(
      atob(base64)
        .split('')
        .map((c) => '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2))
        .join('')
    );

    return JSON.parse(jsonPayload);
  } catch (error) {
    console.error('Failed to decode token:', error);
    return null;
  }
};

// Logout function
export const logout = (): void => {
  removeToken();
};