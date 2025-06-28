import React from 'react';
import './index.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

import StudentDetails from './components/StudentDetails';
import ParentDetails from './components/ParentDetails';
import AcademicRecords from './components/AcademicRecords';
import CareerGuidance from './components/CareerGuidance';
import ReportProblem from './components/ReportProblem';
import Feedback from './components/Feedback';
import StudentDashboard from './components/StudentDashboard';

const Home = () => (
  <div className="container">
    <h1>Student Portal</h1>
    <StudentDetails />
    <ParentDetails />
    <AcademicRecords />
    <CareerGuidance />
    <ReportProblem />
    <Feedback />
  </div>
);

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/dashboard" element={<StudentDashboard />} />
      </Routes>
    </Router>
  );
}

export default App;
