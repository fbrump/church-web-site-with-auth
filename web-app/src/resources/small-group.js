import axios from 'axios'
import getHeaders from '.'

const getAll = async () => {
  return await axios.get('/api-core/small-groups/?skip=0&limit=100', {
    headers: getHeaders()
  })
}

const getById = async (id) => {
  return await axios.get('/api-core/small-groups/' + id, {
    headers: getHeaders()
  })
}

export { getAll, getById }
