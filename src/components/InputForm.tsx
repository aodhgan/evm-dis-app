// @next/next/no-document-import-in-page
"use client"

import React, { useEffect, useState, useRef } from 'react';
import GraphvizRenderer from './GraphvizRenderer';

const InputForm = () => {
    const [inputText, setInputText] = useState<string>('');
    const [apiResponse, setApiResponse] = useState<string>('');
    const [shouldSubmit, setShouldSubmit] = useState<boolean>(false);
    const formRef = useRef<HTMLFormElement>(null);

    useEffect(() => {
        if (shouldSubmit) {
            formRef.current?.dispatchEvent(new Event('submit', { cancelable: true, bubbles: true }));
            setShouldSubmit(false); // Reset the flag
        }
    }, [inputText, shouldSubmit]);

    const handlePresetInput = () => {
        const presetValue = '60015f5b600a81106014575060405260206040f35b905f5b600a8110602c57506001600a91019190506003565b9060020290601756';
        setInputText(presetValue);
        setShouldSubmit(true); // Set the flag to indicate an upcoming submission
    };

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
            <form onSubmit={handleSubmit} ref={formRef}>
                <input
                    type="text"
                    className="w-full p-4 border rounded-lg focus:ring focus:ring-blue-500 focus:outline-none transition ease-in-out duration-150"
                    value={inputText}
                    onChange={(e) => setInputText(e.target.value)}
                    placeholder="Enter bytecode"
                />
                <button type="submit">Submit</button>

            </form>
            <a href="#" onClick={handlePresetInput} style={linkStyle}>Run Example Bytecode</a>
            {apiResponse && <GraphvizRenderer dot={apiResponse} />}
        </div >
    );
};

const linkStyle = {
    paddingTop: '10px', // Or adjust as needed
};

const containerStyle: React.CSSProperties = {
    display: 'flex',
    flexDirection: 'column',
    justifyContent: 'center',
    alignItems: 'center',
    // height: '100vh',
    // textAlign: 'center',
    paddingTop: '50px', // Space on top
    paddingBottom: '20px', // Space on bottom
};

export default InputForm;
