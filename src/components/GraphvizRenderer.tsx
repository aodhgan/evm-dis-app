// src/components/GraphvizRenderer.tsx

import React, { useEffect, useRef, useState } from 'react';
import { Graphviz } from "@hpcc-js/wasm/graphviz";

interface GraphvizRendererProps {
    dot: string;
}

const GraphvizRenderer: React.FC<GraphvizRendererProps> = ({ dot }) => {
    const ref = useRef<HTMLDivElement>(null);
    const [svgContent, setSvgContent] = useState<string>('');

    useEffect(() => {
        let isMounted = true;

        const renderGraph = async () => {
            const graphviz = await Graphviz.load();
            const svg = graphviz.dot(dot);
            if (isMounted) {
                setSvgContent(svg);
            }
        };

        renderGraph();

        return () => {
            isMounted = false;
        };
    }, [dot]);

    return <div ref={ref} dangerouslySetInnerHTML={{ __html: svgContent }} />;
};

export default GraphvizRenderer;
