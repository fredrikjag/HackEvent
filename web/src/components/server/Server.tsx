import Styles from "./Server.module.css"

export interface ServerProps {
  id: string,
  image_link: string,
  ip_addr: string,
  name: string
}

const Server = (props: ServerProps) => {
  return (
    <div className={Styles.ServerHolder}>
      <h2 style={{fontWeight:"bolder", margin:"0"}}>{props.name}</h2>
      <h3 style={{fontWeight:"lighter"}}>{props.ip_addr}</h3>
      <div className={Styles.avatar}>
        <img src={props.image_link}></img>
      </div>
    </div>
  )
}

export default Server