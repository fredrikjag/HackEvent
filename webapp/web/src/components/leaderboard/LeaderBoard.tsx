import React from 'react';
import Styles from './LeaderBoard.module.css';
import { CrownSimple, User } from "@phosphor-icons/react";

interface ContestantProps {
  user_name: string;
  user_time?: string;
  root_time?: string;
  current_placement: string;
}

interface LeaderBoardProps {
  contestantList: ContestantProps[];
}

const DefaultColor = "#BEBDBD";
const UserColor = "#2F6F4D"; 
const RootColor = "#EBC036"; 

const LeaderBoard: React.FC<LeaderBoardProps> = ({ contestantList }) => {

  if (contestantList?.length) {
    return (
      <div className={Styles.LeaderBoard}>
        <ul>
          {contestantList.map((user_props: ContestantProps) => (
              <li key={user_props.current_placement}>
                <div className={Styles.Contestant}>
                  <p className={Styles.CurrentPlacement}> {user_props.current_placement} </p>
                  <div className={Styles.ContestantWrapper}>
                    <div className={Styles.ContestantNameLogos}>
                      <p> {user_props.user_name} </p>
                      {user_props.user_time ? (
                        <User size={25} color={UserColor} weight="fill" />
                      ):
                        <User size={25} color={DefaultColor} weight="fill" />
                      }
                      {user_props.root_time ? (
                        <CrownSimple size={25} color={RootColor} weight="fill" />
                      ):
                        <CrownSimple size={25} color={DefaultColor} weight="fill" />
                      } 
                    </div>
                      <div className={Styles.ContestantTimes}>
                        {user_props.user_time ? <p>U: {user_props.user_time}</p> : <p>U: No time</p>}
                        {user_props.root_time ? <p>R: {user_props.root_time}</p> : <p>R: No time</p>}
                      </div>
                    </div>
                  </div>
              </li>
          ))}
        </ul>
      </div>
    );
  } else {
    return (
      <div className={Styles.Uncompleted}>
        <h4>Be the first to complete the the box </h4>
      </div>
    )
  }
    
};

export default LeaderBoard;
