import { useState } from "react";
import Styles from "./App.module.css"
import EventInfo from './components/eventinfo/EventInfo'
import FlagRegistration from "./components/flag_registration/FlagRegistration";
import LeaderAndServer from "./components/leader_and_server/LeaderboardAndServer";


function App() {

  const [showFlagRegistration, setShowFlagRegistration] = useState(false); 
  
  function displayFlagClick() { setShowFlagRegistration((prevShowFlag) => !prevShowFlag) }

  return (
    <div className={Styles.SiteStyle}>
      {showFlagRegistration ? <FlagRegistration handleClick={displayFlagClick} /> : null}
      <div className={Styles.Container}>
        <EventInfo />
        <LeaderAndServer />
      </div>
    </div>
  )
}

export default App
