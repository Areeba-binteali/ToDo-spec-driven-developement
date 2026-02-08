import '../styles/globals.css';
import '../styles/minimal.css'; // Additional minimal CSS for styling
import type { AppProps } from 'next/app';
import { useRouter } from 'next/router';
import { useEffect } from 'react';

function MyApp({ Component, pageProps }: AppProps) {
  const router = useRouter();

  // Check for auth status on route changes (client-side)
  useEffect(() => {
    // This is where we could implement global auth checks if needed
  }, [router.pathname]);

  return <Component {...pageProps} />;
}

export default MyApp;