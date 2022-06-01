from botocore.exceptions import ClientError
import boto3

cf = boto3.client('cloudformation')


def parse_template(template):
    with open(template) as template_fileobj:
        template_data = template_fileobj.read()
        cf.validate_template(TemplateBody=template_data)
        return template_data


def cf_crete_stack(stack_name, stack_template):
    try:
        cf.create_stack(StackName=stack_name,
                        TemplateBody=parse_template(stack_template)
                        )
        print(f'{stack_name} has been inicialized')
    except ClientError as e:
        print(e)
        return


if __name__ == '__main__':
    cf_crete_stack('kms-btu', './kms.yml')
