// src/components/GraphvizRenderer.tsx

import React, { useEffect, useRef, useState } from 'react';
import { Graphviz } from "@hpcc-js/wasm/graphviz";
import { TransformWrapper, TransformComponent } from 'react-zoom-pan-pinch';
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

    return (
        <TransformWrapper initialScale={1} minScale={0.0001}>
            <TransformComponent>
                <div ref={ref} dangerouslySetInnerHTML={{ __html: svgContent }} />;
            </TransformComponent>
        </TransformWrapper >
    )
};

export default GraphvizRenderer;
