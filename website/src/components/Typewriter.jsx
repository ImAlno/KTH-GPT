import { useState, useEffect, useRef } from 'react';

const Typewriter = ({ text, speed = 30, onUpdate }) => {
    const [displayedText, setDisplayedText] = useState('');
    const onUpdateRef = useRef(onUpdate);
    const indexRef = useRef(0);

    useEffect(() => {
        onUpdateRef.current = onUpdate;
    }, [onUpdate]);

    useEffect(() => {
        setDisplayedText('');
        indexRef.current = 0;

        const timer = setInterval(() => {
            if (indexRef.current < text.length) {
                indexRef.current += 1;
                setDisplayedText(text.slice(0, indexRef.current));
                if (onUpdateRef.current) onUpdateRef.current();
            } else {
                clearInterval(timer);
            }
        }, speed);

        return () => clearInterval(timer);
    }, [text, speed]);

    return <span>{displayedText}</span>;
};

export default Typewriter;
