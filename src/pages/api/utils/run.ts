// utils/runCliTool.ts

import { exec } from 'child_process';

const MAX_BUFFER_SIZE = 2048 * 1024;

const runCliTool = (args: string): Promise<string> => {
    console.log("runCliTool args val ", args)

    return new Promise((resolve, reject) => {
        console.log("running cli tool...") // node src/pages/api/utils/driver
        exec(`python3 evm-dis/build/libs/driver-py/__main__.py --cfg 100 "${args}"`, { maxBuffer: MAX_BUFFER_SIZE }, (error, stdout, stderr) => {
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
