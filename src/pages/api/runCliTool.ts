// pages/api/runCliTool.ts

import type { NextApiRequest, NextApiResponse } from 'next';
import runCliTool from './utils/run';

export default async function handler(req: NextApiRequest, res: NextApiResponse) {
    if (req.method === 'POST') {
        try {
            const { args } = req.body;

            // Invoke your CLI tool logic here.
            const result = `Your CLI tool is processing...: ${args}`;

            const graphResult = await runCliTool(args)

            res.status(200).json(graphResult);
        } catch (error) {
            if (error instanceof Error) {
                res.status(500).json({ message: "Error processing request", error: error.message });
            }
        }
    } else {
        res.setHeader('Allow', ['POST']);
        res.status(405).end(`Method ${req.method} Not Allowed`);
    }
}
