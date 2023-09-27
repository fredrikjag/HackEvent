import { useState, useEffect } from 'react';

interface CountdownTimerProps {
  initialTimeInMilliseconds: number;
}

const CountdownTimer = (props: CountdownTimerProps) => {
  const [timeLeft, setTimeLeft] = useState<number>(props.initialTimeInMilliseconds);

  useEffect(() => {
    const interval = setInterval(() => {
      if (timeLeft > 0) {
        setTimeLeft(timeLeft - 1);
      } else {
        clearInterval(interval);
      }
    }, 1); // Update every 1 millisecond

    return () => {
      clearInterval(interval);
    };
  }, [timeLeft]);

  const minutes = Math.floor(timeLeft / 60000); // Convert milliseconds to minutes
  const seconds = Math.floor((timeLeft % 60000) / 1000); // Convert remaining milliseconds to seconds
  const milliseconds = (timeLeft % 1000).toString().padStart(3, '0'); // Extract and format milliseconds

  return (
    <div>
      {minutes.toString().padStart(2, '0')}:{seconds.toString().padStart(2, '0')}.{milliseconds}
    </div>
  );
};

export default CountdownTimer;
