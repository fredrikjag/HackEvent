
import Styles from './LeaderboardAndServer.module.css'
import Server from '../server/Server'
import LeaderBoard from '../leaderboard/LeaderBoard'
import useFetchServer from '../../hooks/useFetchServer';
import Loading from '../loading/Loading';

const asd = [{
    user_name: "Fredrik Jamshidi",
    user_time: "40:13",
    current_placement: 1
},{
    user_name: "Fredrik Jamshidi",
    user_time: "40:13",
    root_time: "1:31:03",
    current_placement: 2
}];

const LeaderAndServer = () => {

    const {data, httpStatus, callError} = useFetchServer("http://10.254.1.233:5000/api/v1/s/servers")

    console.log(data)
    console.log(httpStatus)
    console.log(callError)


    return (
        <>
        <div className={Styles.ServersContainer}>
            { data 
                ? data.map(ServerProps => { return <Server key={ServerProps.id} id={ServerProps.id} name={ServerProps.name} ip_addr={ServerProps.ip_addr} image_link={'http://10.254.1.233:5000/common/images/' + ServerProps.image_link} />}) 
                : <Loading message={httpStatus}/>
            }
        </div>

        <div className={Styles.LeaderBoardContainer}>
            <div className={Styles.LeaderBoardHead}>
                <h3>Leaderboards</h3> 
                {/* <button onClick={displayFlagClick}>Enter flag</button> */}
            </div>
            <div className={Styles.LeaderBoardHolder}>
                <LeaderBoard contestantList={asd}/>
                <LeaderBoard contestantList={asd}/>
                <LeaderBoard contestantList={asd}/>
            </div>
        </div>
        </>
    )
}

export default LeaderAndServer