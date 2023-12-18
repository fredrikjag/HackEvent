import Styles from './Loading.module.css'

interface LoadingProps {
    message: string
}

const Loading = ({message}: LoadingProps) => {
  return (
    <>
    <div className={Styles.LoadingContainer}>
        <p>{message}<span className={Styles.LoadingDots}>.</span></p>
    </div>
    </>
  )
}

export default Loading