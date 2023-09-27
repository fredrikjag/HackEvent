import { useState } from "react";
import Styles from "./App.module.css"
import LeaderBoard from "./components/leaderboard/LeaderBoard"
import EventInfo from './components/eventinfo/EventInfo'
import FlagRegistration from "./components/flag_registration/FlagRegistration";
import Server from './components/server/Server'


function App() {

  const data = [
    {
      user_name: 'Pelle Johnson',
      user_time: '40.19',

      current_placement: '1',
    },
    {
      user_name: 'Anders Smith',
      user_time: '40.19',
      root_time: '2.31.58',
      current_placement: '2',
    },
    {
      user_name: 'Eva Williams',
      user_time: '25.50',
      root_time: '1.22.37',
      current_placement: '3',
    },
    {
      user_name: 'Lena Davis',
      user_time: '45.05',
      root_time: '2.55.20',
      current_placement: '4',
    },
    {
      user_name: 'John Brown',
      user_time: '33.29',
      root_time: '1.45.18',
      current_placement: '5',
    },
    {
      user_name: 'Alice Miller',
      user_time: '37.42',
      root_time: '2.10.09',
      current_placement: '6',
    },
    {
      user_name: 'Bob Wilson',
      user_time: '28.56',
      root_time: '1.32.47',
      current_placement: '7',
    },
    {
      user_name: 'Sara Lee',
      user_time: '42.37',
      root_time: '2.48.55',
      current_placement: '8',
    },
    {
      user_name: 'Tom Moore',
      user_time: '39.20',
      root_time: '2.15.30',
      current_placement: '9',
    },
    {
      user_name: 'Laura Taylor',
      user_time: '31.45',
      root_time: '1.37.59',
      current_placement: '10',
    },
    {
      user_name: 'Chris Evans',
      user_time: '35.12',
      root_time: '2.05.18',
      current_placement: '11',
    },
    {
      user_name: 'Emily Clark',
      user_time: '29.27',
      root_time: '1.28.55',
      current_placement: '12',
    },
    {
      user_name: 'Daniel Harris',
      user_time: '38.56',
      root_time: '2.22.47',
      current_placement: '13',
    },
    {
      user_name: 'Sophia White',
      user_time: '41.30',
      root_time: '2.40.12',
      current_placement: '14',
    },
    {
      user_name: 'William Hall',
      user_time: '27.18',
      root_time: '1.20.36',
      current_placement: '15',
    },
    {
      user_name: 'Olivia King',
      user_time: '32.05',
      root_time: '1.55.47',
      current_placement: '16',
    },
    {
      user_name: 'Michael Adams',
      user_time: '43.21',
      root_time: '2.52.13',
      current_placement: '17',
    },
    {
      user_name: 'Ava Martinez',
      user_time: '37.58',
      root_time: '2.11.27',
      current_placement: '18',
    },
    {
      user_name: 'James Turner',
      user_time: '31.09',
      root_time: '1.36.25',
      current_placement: '19',
    },
    {
      user_name: 'Grace Allen',
      user_time: '29.45',
      root_time: '1.27.13',
      current_placement: '20',
    }
  ];

  const [showFlagRegistration, setShowFlagRegistration] = useState(false); 
  
  function displayFlagClick() {
    setShowFlagRegistration((prevShowFlag) => !prevShowFlag)
  }

  return (
    <div className={Styles.SiteStyle}>
      <div className={Styles.Container}>
        <EventInfo />
        <div className={Styles.ServersContainer}>
          <Server name='ImBlue' ip='10.40.5.3' imageurl='http://127.0.0.1:5000/images/avatar.jpg' />
          <Server name='OpenSesame' ip='10.40.5.4' imageurl='http://127.0.0.1:5000/images/harry.jpg' />
          <Server name='If-It-Fits' ip='10.40.5.5' imageurl='http://127.0.0.1:5000/images/cat_box.jpg' />
        </div>
            
        <div className={Styles.LeaderBoardContainer}>
          <div className={Styles.LeaderBoardHead}>
            <h3>Leaderboards</h3> 
            <button onClick={displayFlagClick}>Enter flag</button>
          </div>
          <div className={Styles.LeaderBoardHolder}>
            <LeaderBoard contestantList={data}/>
            <LeaderBoard contestantList={data}/>
            <LeaderBoard contestantList={data}/>
          </div>
        </div>
        {showFlagRegistration ? <FlagRegistration handleClick={displayFlagClick} /> : null}
      </div>
    </div>
  )
}

export default App
