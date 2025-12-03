import { useState, useEffect } from 'react';

const AsciiAnimation = ({ frames, speed = 100, className }) => {
    const [frameIndex, setFrameIndex] = useState(0);

    useEffect(() => {
        const timer = setInterval(() => {
            setFrameIndex((prev) => (prev + 1) % frames.length);
        }, speed);

        return () => clearInterval(timer);
    }, [frames, speed]);

    return (
        <pre className={className} style={{ margin: 0, lineHeight: 1, fontFamily: 'monospace' }}>
            {frames[frameIndex]}
        </pre>
    );
};

export default AsciiAnimation;
