import { useEffect, useState } from "react";


const EventInfo = () => {
  const [timeLeft, setTimeLeft] = useState<string>("00:00:00");

  useEffect(() => {
    const eventSource = new EventSource("http://127.0.0.1:5000/api/event/timer");
    
    // attaching a handler to receive message events
    eventSource.onmessage = (event) => {
      // const data = JSON.parse(event.data);
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