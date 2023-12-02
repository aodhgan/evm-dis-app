// utils/runCliTool.ts

import { exec } from 'child_process';

const runCliTool = (args: string): Promise<string> => {
    console.log("runCliTool args val ", args)

    return new Promise((resolve, reject) => {
        console.log("running cli tool...") // build.js --cfg 100 "${args}"
        exec(`node src/pages/api/utils/driver.js --cfg 100 "${args}"`, (error, stdout, stderr) => {
            if (error) {
                reject(new Error(`error: ${error.message}`));
                return;
            }
            if (stderr) {
                reject(new Error(`stderr: ${stderr}`));
                return;
            }
            // Find the index where "digraph" starts
            const digraphIndex = stdout.indexOf('digraph');
            if (digraphIndex === -1) {
                reject(new Error('digraph not found in output'));
                return;
            }

            // Extract everything from "digraph" onwards
            const digraphOutput = stdout.substring(digraphIndex);
            resolve(digraphOutput.trim());
        });
        console.log("exec finished")
    });
};

export default runCliTool;
