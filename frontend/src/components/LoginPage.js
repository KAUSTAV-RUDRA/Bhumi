import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

const LoginPage = () => {
  const [username, setUsername] = useState('');
  const navigate = useNavigate();

  const handleLogin = (e) => {
    e.preventDefault();
    if (/^\d{5}$/.test(username)) {
      navigate('/volunteer-home');
    } else if (username.startsWith('admin_') || username.endsWith('@bhumi.ngo')) {
      navigate('/admin-dashboard');
    } else {
      alert('Invalid username.');
    }
  };

  return (
    <div className="login-container">
      <h2>Login to Bhumi Portal</h2>
      <form onSubmit={handleLogin}>
        <input
          type="text"
          placeholder="Enter username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          required
        />
        <button type="submit">Login</button>
      </form>
    </div>
  );
};

export default LoginPage;
