/*
Name: Angel Avila
Date: 11/24/26
File: useAxios.jsx
Description:
*/

import { useState, useRef } from 'react';
import axios from 'axios';
import settings from "/src/config/settings.jsx";

const useAxios = (resourceURI) => {
    const baseURI = `${settings.baseApiUrl}/${resourceURI}`;
    const [data, setData] = useState(null);
    const [error, setError] = useState(null);
    const [success, setSuccess] = useState(false);
    const [isLoading, setIsLoading] = useState(false);

     const abortController = useRef(null);

    // Centralized promise handler
    const handleResponse = (promise) => {
        promise
            .then(response => {
                setIsLoading(false);
                setError(null);
                setSuccess(true);
                setData(response.data);
            })
            .catch(err => {
                setIsLoading(false);
                if (axios.isCancel(err)) {
                    // setError('Request aborted');
                } else if (err.response) {
                    // Server responded with an error status
                    const data = err.response.data;
                    if (Array.isArray(data.detail)) {
                        // Format each field error with field name and message
                        const formatted = data.detail
                            .map(d => `${d.loc[d.loc.length - 1]}: ${d.msg}`)
                            .join('; ');
                        setError(formatted);
                    } else if (data.detail) {
                        setError(data.detail);
                    } else {
                        setError('An unknown error occurred.');
                    }
                } else {
                    // Other errors (network, timeout, etc.)
                    setError(err.message);
                }
            });
    };

    // Generic request function
    const axiosRequest = (method, url, body = null, params={}) => {
        abortController.current = new AbortController();
        const signal = abortController.current.signal;

        setIsLoading(true);

        const promise = axios({
            method: method,
            url: url,
            data: body,
            params,
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            signal: signal
        });

        handleResponse(promise);
    };

    // Expose abort function
    const abort = () => {
        if (abortController.current) {
            abortController.current.abort();
        }
    };

    // CRUD functions
    const getAll = (params = {}) => {
        return axiosRequest('GET', `${baseURI}/`, null, params);
    };

    const get = (id) => {
        return axiosRequest('GET', `${baseURI}/${id}`);
    };

    return { data, error, isLoading, success, abort, getAll, get};
};

export default useAxios;