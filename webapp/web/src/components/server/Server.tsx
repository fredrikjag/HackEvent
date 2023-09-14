import Styles from "./Server.module.css"

interface ServerProps{
  name: string;
  ip: string;
  imageurl: string;
}

const Server = (props: ServerProps) => {
  return (
    <div className={Styles.ServerHolder}>
      <h2 style={{fontWeight:"bolder", margin:"0"}}>{props.name}</h2>
      <h3 style={{fontWeight:"lighter"}}>{props.ip}</h3>
      <div className={Styles.avatar}>
        <img src={props.imageurl}></img>
      </div>
    </div>
  )
}

export default Server