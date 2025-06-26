import React from 'react';
import { Routes, Route } from 'react-router-dom';
import LoginPage from './components/LoginPage';
import VolunteerHome from './components/VolunteerHome';
import AdminDashboard from './components/AdminDashboard';
import HeroSection from './components/HeroSection';
import MissionSection from './components/MissionSection';
import CTASection from './components/CTASection';
import Footer from './components/Footer';

const App = () => (
  <Routes>
    <Route path="/" element={<LoginPage />} />
    <Route
      path="/volunteer-home"
      element={
        <>
          <HeroSection />
          <MissionSection />
          <CTASection />
          <Footer />
        </>
      }
    />
    <Route path="/admin-dashboard" element={<AdminDashboard />} />
  </Routes>
);
export default App;