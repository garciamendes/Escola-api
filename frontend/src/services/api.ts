// third party
import { isEmpty } from 'lodash'
import { stringify, ParsedQuery } from 'query-string'
import axios, { AxiosRequestConfig } from 'axios'

// local
import { IUrlParams } from './types'
const dj_urls = window.dj_urls

const requests = axios.create({
  headers: {
    'Access-Control-Allow-Origin': '*'
  },
})

export const api = {
  get(url: string, params: IUrlParams = {}, filters: ParsedQuery = {}, config: AxiosRequestConfig = {}) {
    // url = dj_urls[url](params)
    const search = stringify(filters)
    if (!isEmpty(search))
      url = `${url}?${search}`
    return requests.get(url, config)
  },

  post(url: string, params: IUrlParams = {}, data: any, config: AxiosRequestConfig = {}) {
    // url = dj_urls[url](params)
    return requests.post(url, data, config)
  },

  put(url: string, params: IUrlParams = {}, data: any, config: AxiosRequestConfig = {}) {
    // url = dj_urls[url](params)
    return requests.put(url, data, config)
  },

  patch(url: string, params: IUrlParams = {}, data: any, config: AxiosRequestConfig = {}) {
    // url = dj_urls[url](params)
    return requests.patch(url, data, config)
  },

  delete(url: string, params: IUrlParams = {}, config: AxiosRequestConfig = {}) {
    // url = dj_urls[url](params)
    return requests.delete(url, config)
  }
}