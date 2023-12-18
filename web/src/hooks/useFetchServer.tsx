import { useEffect, useState } from 'react'
import { ServerProps } from '../components/server/Server';


const useFetchServer = (url: string) => {
    const [data, setData] = useState<ServerProps[]>();
    const [httpStatus, setHttpStatus] = useState<string>("");
    const [callError, setCallError] = useState<unknown>()

    useEffect(() => {
        const fetchData = async () => {
            setHttpStatus("Loading");

            try {
              const response = await fetch(url);

              if (!response.ok) {
                throw new Error("Failed to fetch data");
              }

              const fetchedData = await response.json();
              setData(fetchedData);
              setHttpStatus("")
            } catch(error) {
              setCallError(error)
            }
        };
          fetchData();
    }, [url]);


  return {data, httpStatus, callError};
}

export default useFetchServer