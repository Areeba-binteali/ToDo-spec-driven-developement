import axios from 'axios';
import { getToken } from './authService';

// Base API URL from environment
const API_BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL;

// Create axios instance with default configuration
const apiClient = axios.create({
  baseURL: API_BASE_URL,
});

// Add request interceptor to include token in headers
apiClient.interceptors.request.use(
  (config) => {
    const token = getToken();
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Add response interceptor to handle errors
apiClient.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      // Token might be expired, redirect to login
      localStorage.removeItem('access_token');
      window.location.href = '/login';
    }
    return Promise.reject(error);
  }
);

// Todo API service functions
export const todoService = {
  // Get all todos for the current user
  getTodos: async () => {
    try {
      const response = await apiClient.get('/todos');
      return response.data;
    } catch (error) {
      throw error;
    }
  },

  // Create a new todo
  createTodo: async (todoData: { title: string; description?: string }) => {
    try {
      const response = await apiClient.post('/todos', todoData);
      return response.data;
    } catch (error) {
      throw error;
    }
  },

  // Update an existing todo
  updateTodo: async (id: string, todoData: { title?: string; description?: string; completed?: boolean }) => {
    try {
      const response = await apiClient.put(`/todos/${id}`, todoData);
      return response.data;
    } catch (error) {
      throw error;
    }
  },

  // Delete a todo
  deleteTodo: async (id: string) => {
    try {
      const response = await apiClient.delete(`/todos/${id}`);
      return response.data;
    } catch (error) {
      throw error;
    }
  },

  // Toggle todo completion status
  toggleTodoCompletion: async (id: string) => {
    try {
      const response = await apiClient.put(`/todos/${id}`, { completed: true });
      return response.data;
    } catch (error) {
      throw error;
    }
  },
};