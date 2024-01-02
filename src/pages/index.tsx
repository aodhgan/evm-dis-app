// src/pages/index.ts

import React from 'react';
import InputForm from '../components/InputForm';
import FooterBanner from '../components/FooterBanner';

const Home: React.FC = () => {


  return (


    <div style={{ padding: '20px 0' }}>
      <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
        <img src="/bytespectorlogo.png" alt="Bytespector Logo" />
      </div>
      <InputForm />
      <FooterBanner />
    </div>
  );
};

export default Home;
