import React from 'react';
import {
    fetchUtils, Admin, Resource
} from 'react-admin';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import CardHeader from '@material-ui/core/CardHeader';
import drfProvider from 'ra-data-drf';
import UserIcon from '@material-ui/icons/AccountCircle';

import {
    Sensor1RuleCreate, Sensor1RuleEdit, Sensor1RuleList, Sensor1RuleShow
} from './sensor1';

import {
    Sensor2RuleCreate, Sensor2RuleEdit, Sensor2RuleList, Sensor2RuleShow
} from './sensor2';

import {
    ResultList, ResultShow
} from './result';

const CSRF_COOKIE_NAME = 'csrftoken'
const CSRF_HEADER_NAME = 'X-CSRFToken'

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const httpClient = (url, options = {}) => {
    console.log(options);
    if (options.method === 'POST' || options.method === 'PUT' || options.method === 'PATCH' || options.method === 'DELETE') {
        var csrftoken = getCookie(CSRF_COOKIE_NAME);
        if (!options.headers) {
            options.headers = new Headers();
        }
        options.headers.set(CSRF_HEADER_NAME, csrftoken);
    }
    return fetchUtils.fetchJson(url, options);
}

const dataProvider = drfProvider('/api/v1', httpClient);

const Dashboard = (props) => (
    <Card>
        <CardHeader title="Welcome to the sensor" />
        <CardContent>Some data</CardContent>
    </Card>
);

const SensorApp = () => (
    <Admin title="Sensor Admin" dashboard={Dashboard} dataProvider={dataProvider} >
        <Resource name="sensor1rule" 
            list={Sensor1RuleList} show={Sensor1RuleShow} edit={Sensor1RuleEdit} create={Sensor1RuleCreate} />

        <Resource name="sensor2rule" 
            list={Sensor2RuleList} show={Sensor2RuleShow} edit={Sensor2RuleEdit} create={Sensor2RuleCreate} />

        <Resource name="result" 
            list={ResultList} show={ResultShow} />
    </Admin>
);

export default SensorApp;
