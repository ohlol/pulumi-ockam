# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['OckamIdentityArgs', 'OckamIdentity']

@pulumi.input_type
class OckamIdentityArgs:
    def __init__(__self__):
        """
        The set of arguments for constructing a OckamIdentity resource.
        """
        pass


@pulumi.input_type
class _OckamIdentityState:
    def __init__(__self__, *,
                 identity: Optional[pulumi.Input[str]] = None,
                 vault: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering OckamIdentity resources.
        :param pulumi.Input[str] identity: The JSON representation of the Ockam identity.
        :param pulumi.Input[str] vault: The JSON representation of the Ockam vault.
        """
        if identity is not None:
            pulumi.set(__self__, "identity", identity)
        if vault is not None:
            pulumi.set(__self__, "vault", vault)

    @property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[str]]:
        """
        The JSON representation of the Ockam identity.
        """
        return pulumi.get(self, "identity")

    @identity.setter
    def identity(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "identity", value)

    @property
    @pulumi.getter
    def vault(self) -> Optional[pulumi.Input[str]]:
        """
        The JSON representation of the Ockam vault.
        """
        return pulumi.get(self, "vault")

    @vault.setter
    def vault(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vault", value)


class OckamIdentity(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 __props__=None):
        """
        Create a OckamIdentity resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[OckamIdentityArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a OckamIdentity resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param OckamIdentityArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(OckamIdentityArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = OckamIdentityArgs.__new__(OckamIdentityArgs)

            __props__.__dict__["identity"] = None
            __props__.__dict__["vault"] = None
        super(OckamIdentity, __self__).__init__(
            'ockam:index/ockamIdentity:OckamIdentity',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            identity: Optional[pulumi.Input[str]] = None,
            vault: Optional[pulumi.Input[str]] = None) -> 'OckamIdentity':
        """
        Get an existing OckamIdentity resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] identity: The JSON representation of the Ockam identity.
        :param pulumi.Input[str] vault: The JSON representation of the Ockam vault.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _OckamIdentityState.__new__(_OckamIdentityState)

        __props__.__dict__["identity"] = identity
        __props__.__dict__["vault"] = vault
        return OckamIdentity(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[str]:
        """
        The JSON representation of the Ockam identity.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def vault(self) -> pulumi.Output[str]:
        """
        The JSON representation of the Ockam vault.
        """
        return pulumi.get(self, "vault")
