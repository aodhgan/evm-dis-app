// src/pages/index.ts

import React from 'react';
import InputForm from '../components/InputForm';

const Home: React.FC = () => {


  return (


    <div style={{ padding: '20px 0' }}>
      <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
        <img src="/bytespectorlogo.png" alt="Bytespector Logo" />
      </div>
      <InputForm />
    </div>
  );
};

export default Home;
