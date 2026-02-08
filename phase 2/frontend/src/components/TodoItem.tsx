import React from 'react';

interface TodoItemProps {
  id: string;
  title: string;
  description?: string;
  completed: boolean;
  createdAt: string;
  updatedAt: string;
  onToggle: (id: string, currentStatus: boolean) => void;
  onDelete: (id: string) => void;
}

const TodoItem: React.FC<TodoItemProps> = ({
  id,
  title,
  description,
  completed,
  createdAt,
  updatedAt,
  onToggle,
  onDelete
}) => {
  const formatDate = (dateString: string) => {
    return new Date(dateString).toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'short',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    });
  };

  return (
    <div
      className={`p-4 border rounded-md mb-2 flex items-start justify-between ${
        completed ? 'bg-green-50' : 'bg-white'
      }`}
    >
      <div className="flex items-start">
        <input
          type="checkbox"
          checked={completed}
          onChange={() => onToggle(id, completed)}
          className="mt-1 mr-3 h-5 w-5"
        />
        <div>
          <h3 className={`font-medium ${completed ? 'line-through text-gray-500' : ''}`}>
            {title}
          </h3>
          {description && (
            <p className={`text-sm mt-1 ${completed ? 'line-through text-gray-500' : 'text-gray-600'}`}>
              {description}
            </p>
          )}
          <div className="text-xs text-gray-500 mt-2">
            Created: {formatDate(createdAt)} | Updated: {formatDate(updatedAt)}
          </div>
        </div>
      </div>
      <button
        onClick={() => onDelete(id)}
        className="text-red-600 hover:text-red-800 text-sm"
      >
        Delete
      </button>
    </div>
  );
};

export default TodoItem;