package shim

import (
	"github.com/hashicorp/terraform-plugin-sdk/v2/helper/schema"
	"github.com/build-trust/terraform-provider-ockam/internal/provider"
)

func Provider() *schema.Provider {
	prov := provider.Provider()
	return prov
}
