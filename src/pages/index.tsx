// src/pages/index.ts

import React from 'react';
import InputForm from '../components/InputForm';

const Home: React.FC = () => {
  return (
    <div>
      <h1>Create a control flow graph: </h1>
      <InputForm />
    </div>
  );
};

export default Home;
