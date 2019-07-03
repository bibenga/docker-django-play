import React from 'react';
import {
    fetchUtils, Admin, Resource, ListGuesser, EditGuesser,
    EditButton, ShowButton, Filter,
    List, Datagrid, TextField, EmailField, ArrayField,
    Edit, Create, Show, SimpleShowLayout, SimpleFormIterator,
    SimpleForm, DisabledInput, TextInput, ArrayInput,
    required, minLength, maxLength
} from 'react-admin';

const Sensor1RuleFilter = (props) => (
    <Filter {...props}>
        <TextInput label="Search" source="search" alwaysOn />
        <TextInput label="Code" source="code" />
    </Filter>
);

const Sensor1RuleList = (props) => (
    <List filters={<Sensor1RuleFilter />} sort={{ field: 'code', order: 'ASC' }} {...props}>
        <Datagrid rowClick="edit">
            <TextField source="id" />
            <TextField source="code" />
            <TextField source="value_expr" />
            <EditButton />
            <ShowButton />
        </Datagrid>
    </List>
);

const Sensor1RuleShow = (props) => (
    <Show title={<Sensor1RuleTitle />} {...props}>
        <SimpleShowLayout>
            <TextField source="id" />
            <TextField source="code" />
            <TextField source="value_expr" />
        </SimpleShowLayout>
    </Show>
);

const Sensor1RuleTitle = ({ record }) => {
    if (record && record.id) {
        let displayName = record.code;
        return <span>Edit sensor 1 rule {displayName}</span>;
    } else {
        return <span>Create new sensor 1 rule</span>;
    }
}

const validateValueExpr = [required()];

const Sensor1RuleCreate = (props) => (
    <Create title={<Sensor1RuleTitle />} {...props}>
        <SimpleForm>
            <TextInput source="code" />
            <TextInput source="value_expr" validate={validateValueExpr} />
        </SimpleForm>
    </Create>
);

const Sensor1RuleEdit = (props) => (
    <Edit title={<Sensor1RuleTitle />} {...props}>
        <SimpleForm >
            <DisabledInput source="id" />
            <TextInput source="code" />
            <TextInput source="value_expr" validate={validateValueExpr} />
        </SimpleForm>
    </Edit>
);

export { Sensor1RuleList, Sensor1RuleShow, Sensor1RuleCreate, Sensor1RuleEdit };

