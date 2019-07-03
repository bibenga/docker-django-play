import React from 'react';
import {
    fetchUtils, Admin, Resource, ListGuesser, EditGuesser,
    EditButton, ShowButton, Filter,
    List, Datagrid, TextField, EmailField, ArrayField,
    Edit, Create, Show, SimpleShowLayout, SimpleFormIterator,
    SimpleForm, DisabledInput, TextInput, ArrayInput,
    required, minLength, maxLength
} from 'react-admin';

const ResultFilter = (props) => (
    <Filter {...props}>
        <TextInput label="Search" source="search" alwaysOn />
        <TextInput label="Sensor" source="sensor__iexact" />
        <TextInput label="Code" source="code__iexact" />
    </Filter>
);

const ResultList = (props) => (
    <List filters={<ResultFilter />} sort={{ field: 'moment', order: 'DESC' }} {...props}>
        <Datagrid rowClick="edit">
        <TextField source="id" />
            <TextField source="sensor" />
            <TextField source="source_id" />
            <TextField source="code" />
            <TextField source="moment" />
            <TextField source="value" />
            <ShowButton />
        </Datagrid>
    </List>
);

const ResultShow = (props) => (
    <Show title={<ResultTitle />} {...props}>
        <SimpleShowLayout>
            <TextField source="id" />
            <TextField source="sensor" />
            <TextField source="source_id" />
            <TextField source="code" />
            <TextField source="moment" />
            <TextField source="value" />
        </SimpleShowLayout>
    </Show>
);

const ResultTitle = ({ record }) => {
    if (record && record.id) {
        let displayName = record.code;
        return <span>Edit sensor 2 rule {displayName}</span>;
    } else {
        return <span>Create new sensor 2 rule</span>;
    }
}

export { ResultList, ResultShow };

