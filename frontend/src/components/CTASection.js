import React from 'react';

const CTASection = () => {
  const handleClick = (type) => {
    console.log(`${type} button clicked`);
  };

  return (
    <section className="cta">
      <h2>Get Involved</h2>
      <button onClick={() => handleClick('Volunteer')} className="btn">Become a Volunteer</button>
      <button onClick={() => handleClick('Donate')} className="btn donate">Donate Now</button>
    </section>
  );
};

export default CTASection;