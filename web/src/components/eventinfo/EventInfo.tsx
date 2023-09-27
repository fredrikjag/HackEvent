import CountdownTimer from "../timer/CountDownTimer";
// import Styles from "./EventInfo.module.css";

const EventInfo = () => {
  return (
    <>
        <h2 style={{margin:"10px 0 0 0"}}>Capture the flag</h2>
        <h1><CountdownTimer initialTimeInMilliseconds={3600000} /></h1>
    </>
  )
}

export default EventInfo