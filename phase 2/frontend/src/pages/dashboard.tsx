import React, { useState, useEffect } from 'react';
import { useRouter } from 'next/router';
import { isAuthenticated, getToken, getUserInfo } from '../services/authService';
import { todoService } from '../services/todoService';
import Layout from '../components/Layout';

interface Todo {
  id: number;
  title: string;
  description: string;
  completed: boolean;
  created_at: string;
  updated_at: string;
}

const DashboardPage: React.FC = () => {
  const router = useRouter();
  const [todos, setTodos] = useState<Todo[]>([]);
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [userInfo, setUserInfo] = useState<any>(null);

  const [loadingAuth, setLoadingAuth] = useState(true);

  useEffect(() => {
    // Delay the authentication check until after component mounts
    const checkAuth = async () => {
      await new Promise(resolve => setTimeout(resolve, 0)); // Ensures client-side execution

      console.log('Checking authentication...');
      if (!isAuthenticated()) {
        console.log('Not authenticated, redirecting to login.');
        router.push('/login');
      } else {
        console.log('Authenticated, setting loadingAuth to false.');
        setLoadingAuth(false);
      }
    };

    checkAuth();
  }, []);

  // Show loading state while checking authentication
  const fetchUserInfo = () => {
    const user = getUserInfo();
    setUserInfo(user);
  };

  const fetchTodos = async () => {
    try {
      setLoading(true);
      const todosData = await todoService.getTodos();
      setTodos(todosData);
      setError('');
    } catch (err: any) {
      setError(err.message || 'Failed to load todos');
      console.error('Error fetching todos:', err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    console.log('loadingAuth changed:', loadingAuth);
    if (!loadingAuth) { // Only run if authentication check is complete and user is logged in
      console.log('Fetching user info and todos...');
      fetchUserInfo();
      fetchTodos();
    }
  }, [loadingAuth]); // Rerun when loadingAuth changes

  if (loadingAuth) {
    return (
      <div className="flex justify-center items-center h-screen">
        <p>Loading...</p>
      </div>
    );
  }

  const handleAddTodo = async (e: React.FormEvent) => {
    e.preventDefault();

    if (!title.trim()) {
      setError('Title is required');
      return;
    }

    try {
      const newTodo = await todoService.createTodo({ title, description });
      setTodos([newTodo, ...todos]);
      setTitle('');
      setDescription('');
      setError('');
    } catch (err: any) {
      setError(err.message || 'Failed to add todo');
      console.error('Error adding todo:', err);
    }
  };

  const toggleTodo = async (id: number) => {
    try {
      const todoToUpdate = todos.find(todo => todo.id === id);
      if (!todoToUpdate) return;

      const updatedTodo = await todoService.updateTodo(id.toString(), {
        ...todoToUpdate,
        completed: !todoToUpdate.completed
      });

      setTodos(todos.map(todo =>
        todo.id === id ? updatedTodo : todo
      ));
    } catch (err: any) {
      setError(err.message || 'Failed to update todo');
      console.error('Error updating todo:', err);
    }
  };

  const handleDeleteTodo = async (id: number) => {
    if (!window.confirm('Are you sure you want to delete this task?')) {
      return;
    }

    try {
      await todoService.deleteTodo(id.toString());
      setTodos(todos.filter(todo => todo.id !== id));
    } catch (err: any) {
      setError(err.message || 'Failed to delete todo');
      console.error('Error deleting todo:', err);
    }
  };

  return (
    <Layout title="Dashboard">
      <div className="min-h-screen bg-black">
        <div className="max-w-5xl mx-auto px-4 py-8">
          <div className="text-center mb-12">
            <h1 className="text-4xl font-bold text-white mb-2">
              {userInfo?.email ? `Welcome back, ${userInfo.email.split('@')[0]}!` : 'Your Tasks'}
            </h1>
            <p className="text-white">Manage your daily tasks and boost your productivity</p>
          </div>

          <div className="bg-black rounded-2xl shadow-xl p-6 mb-8 border-2 border-[#00a5bb]">
            <h2 className="text-2xl font-bold text-white mb-6">Add New Task</h2>

            {error && (
              <div className="bg-[#00a5bb] border-l-4 border-[#000] p-4 mb-6 rounded-lg shadow-sm">
                <div className="flex">
                  <div className="flex-shrink-0">
                    <svg className="h-5 w-5 text-[#000]" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
                      <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clipRule="evenodd" />
                    </svg>
                  </div>
                  <div className="ml-3">
                    <p className="text-sm text-[#000]">{error}</p>
                  </div>
                </div>
              </div>
            )}

            <form onSubmit={handleAddTodo} className="space-y-4">
              <div>
                <label htmlFor="title" className="block text-sm font-medium text-white mb-1">
                  Task Title *
                </label>
                <input
                  type="text"
                  id="title"
                  value={title}
                  onChange={(e) => setTitle(e.target.value)}
                  className="input-field"
                  placeholder="What needs to be done?"
                />
              </div>

              <div>
                <label htmlFor="description" className="block text-sm font-medium text-white mb-1">
                  Description
                </label>
                <textarea
                  id="description"
                  value={description}
                  onChange={(e) => setDescription(e.target.value)}
                  className="input-field min-h-[100px]"
                  placeholder="Add details about your task..."
                />
              </div>

              <div className="pt-4">
                <button
                  type="submit"
                  className="btn-primary w-full"
                >
                  Add Task
                </button>
              </div>
            </form>
          </div>

          <div className="bg-black rounded-2xl shadow-xl p-6 border-2 border-[#00a5bb]">
            <h2 className="text-2xl font-bold text-white mb-6">Your Tasks</h2>

            {loading ? (
              <div className="flex justify-center items-center py-12">
                <div className="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-[#00a5bb]"></div>
              </div>
            ) : todos.length === 0 ? (
              <div className="text-center py-12">
                <div className="mx-auto w-24 h-24 bg-[#00a5bb] rounded-full flex items-center justify-center mb-4">
                  <svg xmlns="http://www.w3.org/2000/svg" className="h-12 w-12 text-[#000]" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
                  </svg>
                </div>
                <h3 className="text-xl font-semibold text-white mb-2">No tasks yet</h3>
                <p className="text-white">Add your first task to get started!</p>
              </div>
            ) : (
              <div className="space-y-4">
                {todos.map((todo) => (
                  <div
                    key={todo.id}
                    className={`p-4 rounded-xl border-2 flex items-start justify-between transition-all duration-300 bg-black border-[#00a5bb] hover:border-[#000] ${todo.completed ? 'opacity-80' : ''}`}
                  >
                    <div className="flex items-start space-x-3 flex-1">
                      <button
                        onClick={() => toggleTodo(todo.id)}
                        className={`flex-shrink-0 w-6 h-6 rounded-full border-2 flex items-center justify-center mt-1 ${
                          todo.completed
                            ? 'border-[#00a5bb] text-[#00a5bb]'
                            : 'border-[#00a5bb] hover:border-[#000] text-white'
                        }`}
                        aria-label={todo.completed ? "Mark as incomplete" : "Mark as complete"}
                      >
                        {todo.completed && (
                          <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M5 13l4 4L19 7"></path>
                          </svg>
                        )}
                      </button>

                      <div className="flex-1">
                        <h3 className={`font-semibold transition-all duration-300 ${
                          todo.completed ? 'text-white line-through' : 'text-white'
                        }`}>
                          {todo.title}
                        </h3>
                        {todo.description && (
                          <p className={`text-white mt-1 transition-all duration-300 ${
                            todo.completed ? 'line-through' : ''
                          }`}>
                            {todo.description}
                          </p>
                        )}
                        <div className="flex items-center mt-2 space-x-4 text-xs text-[#00a5bb]">
                          <span>Created: {new Date(todo.created_at).toLocaleDateString()}</span>
                          {todo.completed && (
                            <span>Completed: {new Date(todo.updated_at).toLocaleDateString()}</span>
                          )}
                        </div>
                      </div>
                    </div>

                    <button
                      onClick={() => handleDeleteTodo(todo.id)}
                      className="flex-shrink-0 ml-4 text-[#00a5bb] hover:text-[#000] transition-colors duration-200"
                      aria-label="Delete task"
                    >
                      <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                        <path fillRule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clipRule="evenodd" />
                      </svg>
                    </button>
                  </div>
                ))}
              </div>
            )}
          </div>
        </div>
      </div>
    </Layout>
  );
};

export default DashboardPage;