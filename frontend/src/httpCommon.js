import Axios from 'axios';

const getBaseUrl = () => {
  let url = 'http://localhost:8000'
  if (process.env.REACT_APP_BASEURL) {
    url = process.env.REACT_APP_BASEURL
  }
  return url
}

const axiosBaseURL = Axios.create({
    baseURL: getBaseUrl()
});

export default axiosBaseURL