import { useEffect, useState } from "react";


const EventInfo = () => {
  const [timeLeft, setTimeLeft] = useState<string>("00:00:00");

  useEffect(() => {
    const eventSource = new EventSource("http://10.254.1.233:5000/api/v1/t/event/timer");
    
    eventSource.onmessage = (event) => {
      console.log(event.data);
      setTimeLeft(event.data);
    };
    
    return () => eventSource.close();
  }, []);


  return (
    <>
        <h2 style={{margin:"10px 0 0 0"}}>Capture the flag</h2>
        <h1>{ timeLeft }</h1>
    </>
  )
}

export default EventInfo