// @next/next/no-document-import-in-page
"use client"

import React, { FormEvent, useState } from 'react';
import GraphvizRenderer from './GraphvizRenderer';

const InputForm = () => {
    const [inputText, setInputText] = useState<string>('');
    const [apiResponse, setApiResponse] = useState<string>('');

    const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
        event.preventDefault();
        try {
            console.log("inputText", inputText)
            const response = await fetch('/api/runCliTool', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ args: inputText }),
            });
            console.log("awiting response")
            const data = await response.json();
            console.log("response.data", data)
            setApiResponse(data);

            console.log(data); // Display or process the output from your CLI tool
        } catch (error) {
            console.error("Error:", error);
        }
    };
    return (
        <div style={containerStyle}>
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    value={inputText}
                    onChange={(e) => setInputText(e.target.value)}
                    placeholder="Enter text"
                />
                <button type="submit">Submit</button>
            </form>
            {apiResponse && <GraphvizRenderer dot={apiResponse} />}
        </div>
    );
};

const containerStyle = {
    display: 'flex',
    flexDirection: 'column',
    justifyContent: 'center',
    alignItems: 'center',
    height: '100vh',
    textAlign: 'center',
    paddingTop: '20px', // Space on top
    paddingBottom: '20px', // Space on bottom
};

export default InputForm;
